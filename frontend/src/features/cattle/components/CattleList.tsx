import { useSuspenseQuery } from "@tanstack/react-query"
import { createCattleQueryOptions } from "../hooks/useListCattle"
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { useDeleteCattle } from "../hooks/useDeleteCattle"
import { EllipsisVertical } from "lucide-react"
import { useState } from "react"
import { EditCattleModal } from "./EditCattleModal"
import type { Cattle } from "../types"

function CattleList() {
    const [selectedCattle, setSelectedCattle] = useState<Cattle | null>(null)

    const { data } = useSuspenseQuery(createCattleQueryOptions())
    const { mutate } = useDeleteCattle()

    return (
        <>
            <Table>
                <TableCaption>Cattle List</TableCaption>
                <TableHeader>
                    <TableRow>
                        <TableHead>Identifier</TableHead>
                        <TableHead>Created at</TableHead>
                        <TableHead>Updated at</TableHead>
                        <TableHead></TableHead>
                        <TableHead></TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    {data.map((cattle) => (
                        <TableRow key={cattle.id}>
                            <TableCell>{cattle.identifier}</TableCell>
                            <TableCell>{cattle.created_at}</TableCell>
                            <TableCell>{cattle.updated_at}</TableCell>
                            <TableCell><EllipsisVertical onClick={() => setSelectedCattle(cattle)} /></TableCell>
                            <TableCell>
                                <Button variant="destructive" size="sm" onClick={() => mutate(cattle.id)}>Delete</Button>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
            <EditCattleModal cattle={selectedCattle} onClose={() => setSelectedCattle(null)} />
        </>

    )
}

export default CattleList