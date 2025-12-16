export interface LandWaitingType {
  date_time: string
  tommorow: AreaType[]
  toon: AreaType[]
  adventure: AreaType[]
  westan: AreaType[]
  world: AreaType[]
  country: AreaType[]
  fantasy: AreaType[]
  other: AreaType[]
}

export interface SeeWaitingType {
  date_time: string
  mediterranean: AreaType[]
  mermaid: AreaType[]
  other: AreaType[]
  mysterious: AreaType[]
  arabian: AreaType[]
  america: AreaType[]
  fantasy: AreaType[]
  port: AreaType[]
  lost: AreaType[]
}

export interface AreaType {
  name: string
  condition: string
  type: string
  tml: string | null
  ohl: string | null
  thl: string | null
}
