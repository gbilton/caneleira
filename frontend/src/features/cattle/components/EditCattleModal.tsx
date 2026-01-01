import { Button } from "@/components/ui/button";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
} from "@/components/ui/dialog"
import { Input } from "@/components/ui/input";
import { useEditCattle } from "../hooks/useEditCattle";
import { useForm } from "react-hook-form";
import { type Cattle, type EditCattleInput } from "../types";

type EditCattleModalProps = {
    onClose: () => void;
    cattle: Cattle | null;
}

export function EditCattleModal({ onClose, cattle }: EditCattleModalProps) {
    const { mutate } = useEditCattle()

    const form = useForm<EditCattleInput>({
        values: {
            identifier: cattle?.identifier || "",
        },
    })

    const submit = () => {
        if (!cattle) return;

        mutate({ id: cattle.id, data: { identifier: form.getValues("identifier") } }, {
            onSuccess: () => {
                onClose();
                form.reset();
            },
        });
    }

    return (
        <Dialog open={cattle !== null} onOpenChange={onClose}>
            <DialogContent>
                <DialogHeader>
                    <DialogTitle>Editar Identificador</DialogTitle>
                    <DialogDescription>
                        Aqui você pode editar o identificador do gado.
                    </DialogDescription>
                    <form onSubmit={form.handleSubmit(submit)}>
                        <Input {...form.register("identifier")} placeholder="Novo Identificador" />
                        <Button className="mt-4">Salvar</Button>
                    </form>
                </DialogHeader>
            </DialogContent>
        </Dialog>
    );
}
