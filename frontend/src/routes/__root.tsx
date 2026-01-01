import { createRootRouteWithContext, Link, Outlet } from '@tanstack/react-router'
import { TanStackRouterDevtools } from '@tanstack/react-router-devtools'
import { Toaster } from 'sonner'
import { QueryClient } from '@tanstack/react-query'

// 1. Define the type for the context you will pass to the router
interface MyRouterContext {
  queryClient: QueryClient
}

const RootLayout = () => (
  <>
    <Toaster />
    <div className="p-2 flex gap-2">
      <Link to="/" className="[&.active]:font-bold">Home</Link>
      <Link to="/about" className="[&.active]:font-bold">About</Link>
      <Link to="/cattle" className="[&.active]:font-bold">Cattle</Link>
    </div>
    <hr />
    <Outlet />
    <hr />
    <div>
      <h1>Footer</h1>
    </div>
    <TanStackRouterDevtools />
  </>
)

// 2. Use createRootRouteWithContext<MyRouterContext>()
export const Route = createRootRouteWithContext<MyRouterContext>()({
  component: RootLayout,
})