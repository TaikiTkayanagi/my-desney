export interface LandWaitingType {
  dateTime: string
  tommorow: AreaType[]
  toon: AreaType[]
  adventure: AreaType[]
  westan: AreaType[]
  world: AreaType[]
  country: AreaType[]
  other: AreaType[]
}

export interface AreaType {
  name: string
  conditions: string
  type: string
}
