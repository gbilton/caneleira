import { createFileRoute } from '@tanstack/react-router'
import CattlePage from '../features/cattle/pages/CattlePage'

export const Route = createFileRoute('/cattle')({
  component: CattlePage,
})
