import { CattleForm } from '../CattleForm'

export function CattlePage() {
    return (
        <div className="p-4">
            <h1 className="text-2xl mb-4">Add New Cattle</h1>
            <CattleForm />
        </div>
    )
}

export default CattlePage