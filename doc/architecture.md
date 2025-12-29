```mermaid
erDiagram
    COMPANY ||--o{ LOAD : operates
    COMPANY ||--o{ DRIVER_SETTLEMENT : issues
    COMPANY ||--o{ TRUCK : owns
    COMPANY ||--o{ TRAILER : owns

    EMPLOYEE ||--o{ LOAD : dispatches

    DRIVER ||--o{ LOAD : hauls
    DRIVER ||--o{ DRIVER_SETTLEMENT : receives

    BROKER ||--o{ LOAD : provides

    LOAD ||--o{ LOAD_CHARGE : has
    LOAD ||--o{ DRIVER_SETTLEMENT_LINE : included_in

    DRIVER_SETTLEMENT ||--o{ DRIVER_SETTLEMENT_LINE : contains
    DRIVER_SETTLEMENT ||--o{ SETTLEMENT_PAYMENT : paid_with

    TRUCK ||--o{ MAINTENANCE_RECORD : serviced_by
    TRAILER ||--o{ MAINTENANCE_RECORD : serviced_by

    MAINTENANCE_RECORD ||--o{ MAINTENANCE_PART_LINE : uses

    COMPANY {
        string name
        string EIN
        boolean active
    }

    EMPLOYEE {
        string email
        string role
        boolean active
    }

    DRIVER {
        string full_name
        string ssn
        string pay_type
        boolean active
    }

    LOAD {
        string load_number
        date pickup_date
        date delivery_date
        string status
    }

    LOAD_CHARGE {
        string charge_type
        float amount
        boolean taxable
    }

    DRIVER_SETTLEMENT {
        date period_start
        date period_end
        string status
        string settlement_number
    }

    DRIVER_SETTLEMENT_LINE {
        string description
        float amount
        string line_type
        boolean taxable
    }

    SETTLEMENT_PAYMENT {
        date payment_date
        float amount
        string reference
    }
