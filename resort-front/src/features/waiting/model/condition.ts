import type { AreaType } from '../types/waitingType'

const condition = (
  value: AreaType['condition'] | AreaType['thl'] | AreaType['ohl'] | AreaType['tml'] | undefined,
) => {
  const extractionWaitTime = () => {
    if (!value) return 0
    const match = value.match(/(\d+)分/)
    return match ? parseInt(match[1] ?? '0') : 0
  }

  const getConditionOrWaitTime = () => {
    if (!value) return 0
    const match = value.match(/(\d+)分/)
    return match ? match[0] : value
  }

  return { extractionWaitTime, getConditionOrWaitTime }
}

export { condition }
