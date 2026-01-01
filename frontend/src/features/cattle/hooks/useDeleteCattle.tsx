import { useMutation, useQueryClient } from "@tanstack/react-query";
import { deleteCattle } from "../api/cattleApi";
import { toast } from "sonner";
import { CATTLE_QUERY_KEYS } from "../constants";

export function useDeleteCattle() {
    const queryClient = useQueryClient();

    return useMutation({
        mutationFn: (id: string) => deleteCattle(id),
        onError: () => {
            toast.error('Failed to delete cattle.')
        },
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: CATTLE_QUERY_KEYS.LIST });
            toast.success('Cattle deleted successfully!')
        },
    })
}