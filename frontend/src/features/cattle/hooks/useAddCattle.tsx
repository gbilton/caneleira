import { useMutation } from '@tanstack/react-query'
import { addCattle } from '../api/cattleApi'
import { type CreateCattleInput } from '../types'

export function useAddCattle() {
    return useMutation({
        mutationFn: (data: CreateCattleInput) => addCattle(data),
    })
}
