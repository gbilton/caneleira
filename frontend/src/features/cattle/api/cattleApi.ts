import axios from 'axios'
import { cattleSchema, type Cattle, type CreateCattleInput } from '../types'
import { toast } from 'sonner'

export async function addCattle(data: CreateCattleInput) {
  const response = await axios.post('http://localhost:8008/cattle', data)
  return response.data
}

export async function fetchCattle(): Promise<Cattle[]> {
  const response = await axios.get('http://localhost:8008/cattle')
  const parsedData = cattleSchema.array().safeParse(response.data)

  if (!parsedData.success) {
    toast.error('Failed to parse cattle data')
    console.log('Parsing errors:', parsedData.error)
  }
  return response.data
}

export async function deleteCattle(id: string): Promise<void> {
  await axios.delete(`http://localhost:8008/cattle/${id}`)
}

export async function editCattle(id: string, data: Partial<CreateCattleInput>) {
  const response = await axios.put(`http://localhost:8008/cattle/${id}`, data)
  return response.data
}