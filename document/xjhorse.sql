CREATE TABLE account_emailaddress (
  id       INTEGER      NOT NULL,
  verified BOOL         NOT NULL,
  PRIMARY BOOL NOT NULL,
  user_id  INTEGER      NOT NULL,
  email    VARCHAR(254) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_account_emailaddress_auth_user_1 FOREIGN KEY (user_id) REFERENCES auth_user (id)
);

CREATE INDEX account_emailaddress_e8701ad4
  ON account_emailaddress (user_id ASC);

CREATE TABLE account_emailconfirmation (
  id               INTEGER     NOT NULL,
  created          DATETIME    NOT NULL,
  sent             DATETIME,
  key              VARCHAR(64) NOT NULL,
  email_address_id INTEGER     NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_account_emailconfirmation_account_emailaddress_1 FOREIGN KEY (email_address_id) REFERENCES account_emailaddress (id)
);

CREATE INDEX account_emailconfirmation_6f1edeac
  ON account_emailconfirmation (email_address_id ASC);

CREATE TABLE auth_group (
  id   INTEGER     NOT NULL,
  name VARCHAR(80) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE auth_group_permissions (
  id            INTEGER NOT NULL,
  group_id      INTEGER NOT NULL,
  permission_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_auth_group_permissions_auth_group_1 FOREIGN KEY (group_id) REFERENCES auth_group (id),
  CONSTRAINT fk_auth_group_permissions_auth_permission_1 FOREIGN KEY (permission_id) REFERENCES auth_permission (id)
);

CREATE UNIQUE INDEX auth_group_permissions_group_id_0cd325b0_uniq
  ON auth_group_permissions (group_id ASC, permission_id ASC);
CREATE INDEX auth_group_permissions_0e939a4f
  ON auth_group_permissions (group_id ASC);
CREATE INDEX auth_group_permissions_8373b171
  ON auth_group_permissions (permission_id ASC);

CREATE TABLE auth_permission (
  id              INTEGER      NOT NULL,
  content_type_id INTEGER      NOT NULL,
  codename        VARCHAR(100) NOT NULL,
  name            VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_auth_permission_django_content_type_1 FOREIGN KEY (content_type_id) REFERENCES django_content_type (id)
);

CREATE UNIQUE INDEX auth_permission_content_type_id_01ab375a_uniq
  ON auth_permission (content_type_id ASC, codename ASC);
CREATE INDEX auth_permission_417f1b1c
  ON auth_permission (content_type_id ASC);

CREATE TABLE auth_user (
  id           INTEGER      NOT NULL,
  password     VARCHAR(128) NOT NULL,
  last_login   DATETIME,
  is_superuser BOOL         NOT NULL,
  first_name   VARCHAR(30)  NOT NULL,
  last_name    VARCHAR(30)  NOT NULL,
  email        VARCHAR(254) NOT NULL,
  is_staff     BOOL         NOT NULL,
  is_active    BOOL         NOT NULL,
  date_joined  DATETIME     NOT NULL,
  username     VARCHAR(150) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE auth_user_groups (
  id       INTEGER NOT NULL,
  user_id  INTEGER NOT NULL,
  group_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_auth_user_groups_auth_user_1 FOREIGN KEY (user_id) REFERENCES auth_user (id),
  CONSTRAINT fk_auth_user_groups_auth_group_1 FOREIGN KEY (group_id) REFERENCES auth_group (id)
);

CREATE UNIQUE INDEX auth_user_groups_user_id_94350c0c_uniq
  ON auth_user_groups (user_id ASC, group_id ASC);
CREATE INDEX auth_user_groups_e8701ad4
  ON auth_user_groups (user_id ASC);
CREATE INDEX auth_user_groups_0e939a4f
  ON auth_user_groups (group_id ASC);

CREATE TABLE auth_user_user_permissions (
  id            INTEGER NOT NULL,
  user_id       INTEGER NOT NULL,
  permission_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_auth_user_user_permissions_auth_user_1 FOREIGN KEY (user_id) REFERENCES auth_user (id),
  CONSTRAINT fk_auth_user_user_permissions_auth_permission_1 FOREIGN KEY (permission_id) REFERENCES auth_permission (id)
);

CREATE UNIQUE INDEX auth_user_user_permissions_user_id_14a6b632_uniq
  ON auth_user_user_permissions (user_id ASC, permission_id ASC);
CREATE INDEX auth_user_user_permissions_e8701ad4
  ON auth_user_user_permissions (user_id ASC);
CREATE INDEX auth_user_user_permissions_8373b171
  ON auth_user_user_permissions (permission_id ASC);

CREATE TABLE django_admin_log (
  id              INTEGER      NOT NULL,
  object_id       TEXT,
  object_repr     VARCHAR(200) NOT NULL,
  action_flag     SMALLINT unsigned NOT NULL,
  change_message  TEXT         NOT NULL,
  content_type_id INTEGER,
  user_id         INTEGER      NOT NULL,
  action_time     DATETIME     NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_django_admin_log_django_content_type_1 FOREIGN KEY (content_type_id) REFERENCES django_content_type (id),
  CONSTRAINT fk_django_admin_log_auth_user_1 FOREIGN KEY (user_id) REFERENCES auth_user (id)
);

CREATE INDEX django_admin_log_417f1b1c
  ON django_admin_log (content_type_id ASC);
CREATE INDEX django_admin_log_e8701ad4
  ON django_admin_log (user_id ASC);

CREATE TABLE django_content_type (
  id        INTEGER      NOT NULL,
  app_label VARCHAR(100) NOT NULL,
  model     VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

CREATE UNIQUE INDEX django_content_type_app_label_76bd3d3b_uniq
  ON django_content_type (app_label ASC, model ASC);

CREATE TABLE django_migrations (
  id      INTEGER      NOT NULL,
  app     VARCHAR(255) NOT NULL,
  name    VARCHAR(255) NOT NULL,
  applied DATETIME     NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE django_session (
  session_key  VARCHAR(40) NOT NULL,
  session_data TEXT        NOT NULL,
  expire_date  DATETIME    NOT NULL,
  PRIMARY KEY (session_key)
);

CREATE INDEX django_session_de54fa62
  ON django_session (expire_date ASC);

CREATE TABLE django_site (
  id     INTEGER      NOT NULL,
  name   VARCHAR(50)  NOT NULL,
  domain VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE socialaccount_socialaccount (
  id          INTEGER      NOT NULL,
  provider    VARCHAR(30)  NOT NULL,
  uid         VARCHAR(191) NOT NULL,
  last_login  DATETIME     NOT NULL,
  date_joined DATETIME     NOT NULL,
  user_id     INTEGER      NOT NULL,
  extra_data  TEXT         NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_socialaccount_socialaccount_auth_user_1 FOREIGN KEY (user_id) REFERENCES auth_user (id)
);

CREATE UNIQUE INDEX socialaccount_socialaccount_provider_fc810c6e_uniq
  ON socialaccount_socialaccount (provider ASC, uid ASC);
CREATE INDEX socialaccount_socialaccount_e8701ad4
  ON socialaccount_socialaccount (user_id ASC);

CREATE TABLE socialaccount_socialapp (
  id        INTEGER      NOT NULL,
  provider  VARCHAR(30)  NOT NULL,
  name      VARCHAR(40)  NOT NULL,
  client_id VARCHAR(191) NOT NULL,
  key       VARCHAR(191) NOT NULL,
  secret    VARCHAR(191) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE socialaccount_socialapp_sites (
  id           INTEGER NOT NULL,
  socialapp_id INTEGER NOT NULL,
  site_id      INTEGER NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_socialaccount_socialapp_sites_socialaccount_socialapp_1 FOREIGN KEY (socialapp_id) REFERENCES socialaccount_socialapp (id),
  CONSTRAINT fk_socialaccount_socialapp_sites_django_site_1 FOREIGN KEY (site_id) REFERENCES django_site (id)
);

CREATE UNIQUE INDEX socialaccount_socialapp_sites_socialapp_id_71a9a768_uniq
  ON socialaccount_socialapp_sites (socialapp_id ASC, site_id ASC);
CREATE INDEX socialaccount_socialapp_sites_fe95b0a0
  ON socialaccount_socialapp_sites (socialapp_id ASC);
CREATE INDEX socialaccount_socialapp_sites_9365d6e7
  ON socialaccount_socialapp_sites (site_id ASC);

CREATE TABLE socialaccount_socialtoken (
  id           INTEGER NOT NULL,
  token        TEXT    NOT NULL,
  token_secret TEXT    NOT NULL,
  expires_at   DATETIME,
  account_id   INTEGER NOT NULL,
  app_id       INTEGER NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_socialaccount_socialtoken_socialaccount_socialaccount_1 FOREIGN KEY (account_id) REFERENCES socialaccount_socialaccount (id),
  CONSTRAINT fk_socialaccount_socialtoken_socialaccount_socialapp_1 FOREIGN KEY (app_id) REFERENCES socialaccount_socialapp (id)
);

CREATE UNIQUE INDEX socialaccount_socialtoken_app_id_fca4e0ac_uniq
  ON socialaccount_socialtoken (app_id ASC, account_id ASC);
CREATE INDEX socialaccount_socialtoken_8a089c2a
  ON socialaccount_socialtoken (account_id ASC);
CREATE INDEX socialaccount_socialtoken_f382adfe
  ON socialaccount_socialtoken (app_id ASC);

CREATE TABLE sqlite_sequence (
  name,
  seq
);

