import { type QueryClient, QueryClientProvider } from "@tanstack/react-query"

export function Providers({ queryClient, children }: { queryClient: QueryClient, children: React.ReactNode }) {
    return (
        <QueryClientProvider client={queryClient}>
            {children}
        </QueryClientProvider>
    )
}
