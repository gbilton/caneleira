import { useMutation, useQueryClient } from '@tanstack/react-query'
import { addCattle } from '../api/cattleApi'
import { type CreateCattleInput } from '../types'
import { CATTLE_QUERY_KEYS } from '../constants';
import { toast } from 'sonner';

export function useAddCattle() {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: (data: CreateCattleInput) => addCattle(data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: CATTLE_QUERY_KEYS.LIST });
            toast.success('Cattle added successfully!')
        },
        onError: () => {
            toast.error('Failed to add cattle.')
        }
    })
}
