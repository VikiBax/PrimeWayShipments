erDiagram
  COMPANY ||--o{ LOAD : owns
  BROKER  ||--o{ LOAD : provides
  DRIVER  ||--o{ LOAD : hauls
  LOAD    ||--o{ LOAD_CHARGE : has
  DRIVER  ||--o{ SETTLEMENT : paid_by
  SETTLEMENT ||--o{ SETTLEMENT_LINE : includes
  SETTLEMENT ||--o{ SETTLEMENT_PAYMENT : paid_with
