import { CattleForm } from '../CattleForm'
import CattleList from '../components/CattleList'

export function CattlePage() {
    return (
        <div className="p-4">
            <CattleList />
            <CattleForm />
        </div>
    )
}

export default CattlePage