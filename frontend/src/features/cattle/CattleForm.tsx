import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { createCattleSchema, type CreateCattleInput } from './types'
import { useAddCattle } from './hooks/useAddCattle'
import { Button } from '../../components/ui/button'
import { Input } from '@/components/ui/input'
import { toast } from 'sonner'

export function CattleForm() {
    const { register, handleSubmit, reset, formState: { errors } } = useForm<CreateCattleInput>({
        resolver: zodResolver(createCattleSchema)
    })

    const { mutate, isPending } = useAddCattle()

    const onSubmit = (data: CreateCattleInput) => {
        mutate(data, {
            onSuccess: () => {
                toast.success('Cattle added successfully!')
                reset()
            },
            onError: () => toast.error('Failed to add cattle'),
        })
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-2 max-w-sm">
            <h1 className="text-2xl mb-4">Add New Cattle</h1>
            <label>
                Identifier
                <Input type="text" {...register('identifier')} />
                {errors.identifier && <span className="text-red-500">{errors.identifier.message}</span>}
            </label>
            <Button type='submit' disabled={isPending}>
                {isPending ? 'Adding...' : 'Add Cattle'}
            </Button>
        </form>
    )
}
