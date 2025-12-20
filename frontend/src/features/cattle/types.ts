import { z } from 'zod'

// Input for creating a cattle
export const createCattleSchema = z.object({
  identifier: z.string().min(1, 'Identifier is required'),
})

// Type inferred from Zod
export type CreateCattleInput = z.infer<typeof createCattleSchema>
