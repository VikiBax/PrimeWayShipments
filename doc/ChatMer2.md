```mermaid 
erDiagram
    %% =========================
    %% Core entities (you have)
    %% =========================

    COMPANY {
      int id PK
      string name
      bool active
      string ein
      int next_load_number
      int next_settlement_number
      string load_prefix
      string settlement_prefix
      datetime created_at
      datetime updated_at
    }

    EMPLOYEE {
      int id PK
      string username
      string email
      string role
      bool is_active
    }

    DRIVER {
      int id PK
      string first_name
      string last_name
      string phone
      string email
      string ssn_last4
      string ssn_full
      string status
      string pay_type
      decimal default_percent
      decimal default_cpm
      decimal default_flat
      bool default_refunds_taxable
      string notes
    }

    TRUCK {
      int id PK
      string unit_number
      string vin
      string status
      date registration_expiration
      date inspection_expiration
      string notes
    }

    TRAILER {
      int id PK
      string unit_number
      string vin
      string trailer_type
      string status
      date registration_expiration
      date inspection_expiration
      string notes
    }

    %% =========================
    %% Operations (dispatch)
    %% Broker parent + alias model
    %% =========================

    BROKER_COMPANY {
      int id PK
      string name
      string mc_number
      string dot_number
      string billing_email
      string billing_phone
      bool active
      string notes
    }

    BROKER_ALIAS {
      int id PK
      int broker_company_id FK
      string display_name
      string email
      string phone
      bool active
    }

    LOAD {
      int id PK
      int company_id FK
      int broker_alias_id FK
      int driver_id FK
      int dispatcher_id FK
      int truck_id FK
      int trailer_id FK

      string load_number
      datetime pickup_scheduled
      datetime pickup_actual
      datetime delivery_scheduled
      datetime delivery_actual

      string empty_location
      string pickup_location
      string dropoff_location

      string contact_name
      string contact_phone
      string contact_email

      decimal base_rate
      decimal miles
      string status
      datetime locked_at

      string notes
      datetime created_at
      datetime updated_at
    }

    LOAD_CHARGE {
      int id PK
      int load_id FK
      string charge_type
      string description
      decimal amount
      string direction
      bool taxable
      datetime created_at
    }

    %% =========================
    %% Settlements (money)
    %% =========================

    DRIVER_SETTLEMENT {
      int id PK
      int driver_id FK
      int company_id FK
      date period_start
      date period_end
      string settlement_number
      string status
      string notes
      datetime created_at
      datetime updated_at
    }

    DRIVER_SETTLEMENT_LINE {
      int id PK
      int settlement_id FK
      int load_id FK  "nullable"
      string description
      decimal amount
      string line_type
      bool taxable
      datetime created_at
    }

    SETTLEMENT_PAYMENT {
      int id PK
      int settlement_id FK
      date payment_date
      decimal amount
      string method_reference
      string notes
      datetime created_at
    }

    %% =========================
    %% Maintenance / Audit (shown as stubs)
    %% =========================

    MAINTENANCE_RECORD {
      int id PK
      int truck_id FK "nullable"
      int trailer_id FK "nullable"
      date date
      int odometer
      string description
      string vendor
      decimal total_cost
      string notes
    }

    MAINTENANCE_PART_LINE {
      int id PK
      int maintenance_record_id FK
      string part_name
      int quantity
      decimal unit_cost
      decimal total_cost
    }

    AUDIT_EVENT {
      int id PK
      string actor
      string action
      string object_type
      int object_id
      datetime created_at
    }

    %% =========================
    %% Relationships
    %% =========================

    COMPANY ||--o{ LOAD : "has"
    COMPANY ||--o{ DRIVER_SETTLEMENT : "has"
    COMPANY ||--o{ TRUCK : "owns/assigns (optional)"
    COMPANY ||--o{ TRAILER : "owns/assigns (optional)"

    EMPLOYEE ||--o{ LOAD : "dispatches"

    DRIVER ||--o{ LOAD : "runs"
    DRIVER ||--o{ DRIVER_SETTLEMENT : "paid via"

    TRUCK ||--o{ LOAD : "used on"
    TRAILER ||--o{ LOAD : "used on"

    BROKER_COMPANY ||--o{ BROKER_ALIAS : "has aliases"
    BROKER_ALIAS ||--o{ LOAD : "listed on"

    LOAD ||--o{ LOAD_CHARGE : "has charges"

    DRIVER_SETTLEMENT ||--o{ DRIVER_SETTLEMENT_LINE : "has lines"
    DRIVER_SETTLEMENT ||--o{ SETTLEMENT_PAYMENT : "has payments"
    LOAD ||--o{ DRIVER_SETTLEMENT_LINE : "referenced by (optional)"

    TRUCK ||--o{ MAINTENANCE_RECORD : "maintenance"
    TRAILER ||--o{ MAINTENANCE_RECORD : "maintenance"
    MAINTENANCE_RECORD ||--o{ MAINTENANCE_PART_LINE : "parts"
