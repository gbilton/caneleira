import { z } from 'zod'

// Input for creating a cattle
export const createCattleSchema = z.object({
  identifier: z.string().min(1, 'Identifier is required'),
})
// Type inferred from Zod
export type CreateCattleInput = z.infer<typeof createCattleSchema>

export const editCattleSchema = createCattleSchema.partial()
export type EditCattleInput = z.infer<typeof editCattleSchema>


// Cattle type
export const cattleSchema = z.object({
  id: z.string(),
  identifier: z.string(),
  created_at: z.string(),
  updated_at: z.string().nullable(),
})

export type Cattle = z.infer<typeof cattleSchema>