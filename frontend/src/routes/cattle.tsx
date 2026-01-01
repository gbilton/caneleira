import { createFileRoute } from '@tanstack/react-router'
import CattlePage from '../features/cattle/pages/CattlePage'
import { createCattleQueryOptions } from '@/features/cattle/hooks/useListCattle'

export const Route = createFileRoute('/cattle')({
  component: CattlePage,
  loader: async ({ context }) => {
    await context.queryClient.ensureQueryData(createCattleQueryOptions())
  }
})
