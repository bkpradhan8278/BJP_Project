-- Election Intelligence & Analytics Command Center -- CONCEPTUAL schema (PostgreSQL, POC)
-- Design rule: aggregate or appropriately authorised operational records only.
-- There is NO table of individuals' political beliefs, preferences or vote intentions.
-- Survey responses are anonymous/pseudonymised, coarse demographic bins only, used for weighted aggregates.

CREATE EXTENSION IF NOT EXISTS vector;  -- pgvector, for RAG / similarity search

CREATE TABLE campaign (
  campaign_id      TEXT PRIMARY KEY,
  name             TEXT NOT NULL,
  phase            TEXT CHECK (phase IN ('pre_campaign','campaign','high_intensity','final','poll_day','post_poll')),
  start_date       DATE, end_date DATE
);

CREATE TABLE geography (
  geo_id           TEXT PRIMARY KEY,           -- official code where available
  parent_geo_id    TEXT REFERENCES geography(geo_id),
  level            TEXT CHECK (level IN ('state','district','pc','ac','block','ward','zone')),
  name             TEXT NOT NULL,
  boundary_source  TEXT, boundary_version TEXT  -- e.g. 'Survey of India', delimitation vintage
);

CREATE TABLE constituency (
  constituency_id  TEXT PRIMARY KEY REFERENCES geography(geo_id),
  type             TEXT CHECK (type IN ('AC','PC')),
  state            TEXT, reserved_category TEXT  -- public information
);

CREATE TABLE historical_election (           -- public ECI statistical reports
  constituency_id  TEXT REFERENCES constituency(constituency_id),
  election_year    INT, election_type TEXT,
  electors         INT, votes_polled INT, turnout_pct NUMERIC(5,2),
  party            TEXT, vote_share_pct NUMERIC(5,2),
  source_id        TEXT,
  PRIMARY KEY (constituency_id, election_year, election_type, party)
);

CREATE TABLE data_source (                   -- Source & lawful-basis registry
  source_id        TEXT PRIMARY KEY,
  name             TEXT NOT NULL, owner TEXT NOT NULL, steward TEXT,
  family           TEXT CHECK (family IN ('public','campaign_owned','survey','digital','media','field','call_centre')),
  lawful_basis     TEXT NOT NULL,              -- consent / authorisation / licence / public
  authorisation_ref TEXT,                      -- evidence document id
  permitted_purposes TEXT[] NOT NULL,          -- enforced at query time
  sensitivity      TEXT CHECK (sensitivity IN ('public','internal','confidential')),
  refresh_cadence  TEXT, retention_days INT, deletion_method TEXT,
  api_verified_on  DATE, credential_ref TEXT   -- vault reference, never the secret
);

CREATE TABLE data_quality (
  dq_run_id        BIGSERIAL PRIMARY KEY,
  source_id        TEXT REFERENCES data_source(source_id),
  test_name        TEXT, status TEXT CHECK (status IN ('pass','warn','fail')),
  rows_affected    INT, score NUMERIC(5,2), run_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE issue (
  issue_id         TEXT PRIMARY KEY, parent_issue_id TEXT REFERENCES issue(issue_id),
  name             TEXT NOT NULL, description TEXT
);

CREATE TABLE survey (
  survey_id        TEXT PRIMARY KEY, campaign_id TEXT REFERENCES campaign(campaign_id),
  wave             INT, mode TEXT, vendor TEXT, design TEXT,
  fieldwork_start  DATE, fieldwork_end DATE, target_n INT, weighting_scheme TEXT
);

CREATE TABLE survey_question (
  question_id      TEXT PRIMARY KEY, survey_id TEXT REFERENCES survey(survey_id),
  wording          JSONB,                      -- per language
  scale            TEXT, version INT
);

CREATE TABLE survey_response (               -- anonymous; no names, phones, addresses, voter IDs
  response_id      TEXT PRIMARY KEY, survey_id TEXT REFERENCES survey(survey_id),
  age_band TEXT, gender TEXT, area_type TEXT, zone_geo_id TEXT REFERENCES geography(geo_id),
  answers          JSONB,                      -- issue / awareness / satisfaction items
  weight           NUMERIC(8,4),
  qc_speeder BOOLEAN, qc_straightliner BOOLEAN, consent_recorded BOOLEAN NOT NULL
);

CREATE TABLE digital_channel (
  channel_id       TEXT PRIMARY KEY, platform TEXT, handle TEXT, owner TEXT, token_ref TEXT
);

CREATE TABLE content (
  content_id       TEXT PRIMARY KEY, channel_id TEXT REFERENCES digital_channel(channel_id),
  format TEXT, theme TEXT, language TEXT, length_units INT,
  published_at     TIMESTAMPTZ, ai_flag BOOLEAN DEFAULT FALSE
);

CREATE TABLE content_performance (
  content_id       TEXT REFERENCES content(content_id), day DATE,
  impressions BIGINT, reach BIGINT, engagements BIGINT, shares INT, comments INT,
  video_views BIGINT, avg_watch_pct NUMERIC(5,4), clicks BIGINT, spend_inr NUMERIC(12,2),
  PRIMARY KEY (content_id, day)
);

CREATE TABLE media_mention (
  mention_id       TEXT PRIMARY KEY, published_at TIMESTAMPTZ,
  outlet TEXT, outlet_type TEXT, language TEXT, issue_id TEXT REFERENCES issue(issue_id),
  tone TEXT, tone_confidence NUMERIC(4,3), reach_tier TEXT, url TEXT, licence_ref TEXT
);

CREATE TABLE sentiment_record (              -- AGGREGATED public social data
  day DATE, platform TEXT, issue_id TEXT REFERENCES issue(issue_id), language TEXT,
  zone_geo_id TEXT REFERENCES geography(geo_id),  -- only where public location metadata is permitted
  n_mentions INT, n_positive INT, n_neutral INT, n_negative INT,
  mean_score NUMERIC(5,3), coverage_index NUMERIC(5,2), model_version TEXT
);

CREATE TABLE event (
  event_id TEXT PRIMARY KEY, zone_geo_id TEXT REFERENCES geography(geo_id),
  event_type TEXT, event_date DATE, attendance_estimate INT
);

CREATE TABLE field_activity (
  activity_id TEXT PRIMARY KEY, zone_geo_id TEXT REFERENCES geography(geo_id),
  event_id TEXT REFERENCES event(event_id), activity_type TEXT, activity_date DATE,
  planned BOOLEAN, completed BOOLEAN, issue_reports INT,
  report_on_time BOOLEAN, report_quality NUMERIC(3,2)
);

CREATE TABLE operational_metric (            -- call-centre & ops aggregates, no caller PII
  metric_id TEXT, day DATE, unit_geo_id TEXT REFERENCES geography(geo_id),
  dimension JSONB, value NUMERIC, PRIMARY KEY (metric_id, day, unit_geo_id, dimension)
);

CREATE TABLE campaign_spend (
  spend_id TEXT PRIMARY KEY, campaign_id TEXT REFERENCES campaign(campaign_id),
  channel TEXT, vendor TEXT, category TEXT, amount_inr NUMERIC(14,2), spend_date DATE,
  content_id TEXT REFERENCES content(content_id), certification_ref TEXT
);

CREATE TABLE compliance_record (
  record_id BIGSERIAL PRIMARY KEY, content_id TEXT REFERENCES content(content_id),
  approval_status TEXT, approver TEXT, approved_at TIMESTAMPTZ,
  certification_status TEXT, certification_ref TEXT,
  ai_label_status TEXT, ai_label_text TEXT, responsible_entity_disclosed BOOLEAN,
  ai_tool TEXT, ai_creator TEXT, likeness_consent_ref TEXT,
  takedown_notice_at TIMESTAMPTZ, takedown_done_at TIMESTAMPTZ
);

CREATE TABLE audit_log (                     -- append-only; revoke UPDATE/DELETE for all roles
  audit_id BIGSERIAL PRIMARY KEY, at TIMESTAMPTZ DEFAULT now(),
  actor TEXT, action TEXT, object_type TEXT, object_id TEXT, detail JSONB
);

CREATE TABLE alert (
  alert_id TEXT PRIMARY KEY, rule_id TEXT, severity TEXT CHECK (severity IN ('critical','high','medium','low')),
  entity TEXT, evidence JSONB, status TEXT, owner TEXT,
  raised_at TIMESTAMPTZ, acked_at TIMESTAMPTZ, closed_at TIMESTAMPTZ, closure_note TEXT
);

CREATE TABLE report (
  report_id TEXT PRIMARY KEY, report_type TEXT, period_start DATE, period_end DATE,
  version INT, approver TEXT, approved_at TIMESTAMPTZ, uri TEXT
);

CREATE TABLE model_run (
  run_id BIGSERIAL PRIMARY KEY, model_name TEXT, model_version TEXT,
  data_window TSTZRANGE, metrics JSONB, approval_status TEXT, run_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE document_chunk (                -- RAG knowledge base (approved documents only)
  chunk_id BIGSERIAL PRIMARY KEY, doc_id TEXT, doc_type TEXT, page INT,
  allowed_roles TEXT[], published_on DATE, text TEXT, embedding vector(768)
);
