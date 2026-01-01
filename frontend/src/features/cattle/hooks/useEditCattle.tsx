import { useMutation, useQueryClient } from "@tanstack/react-query";
import { editCattle } from "../api/cattleApi";
import type { EditCattleInput } from "../types";
import { toast } from "sonner";


export function useEditCattle() {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: ({ id, data }: { id: string; data: EditCattleInput }) => editCattle(id, data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: ['cattle'] });
            toast.success('Cattle edited successfully!')
        },
        onError: () => {
            toast.error('Failed to edit cattle.')
        }
    })
}

