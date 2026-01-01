import { fetchCattle } from "../api/cattleApi"
import { CATTLE_QUERY_KEYS } from "../constants"


export function createCattleQueryOptions() {
    return {
        queryKey: CATTLE_QUERY_KEYS.LIST,
        queryFn: fetchCattle,
    }
}

