import axios from 'axios'
import type { CreateCattleInput } from '../types'

export async function addCattle(data: CreateCattleInput) {
  const response = await axios.post('http://localhost:8008/cattle', data)
  return response.data
}
