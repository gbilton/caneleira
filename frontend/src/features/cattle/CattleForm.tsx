import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { createCattleSchema, type CreateCattleInput } from './types'
import { useAddCattle } from './hooks/useAddCattle'

export function CattleForm() {
    const { register, handleSubmit, reset, formState: { errors } } = useForm<CreateCattleInput>({
        resolver: zodResolver(createCattleSchema)
    })

    const { mutate, isPending } = useAddCattle()

    const onSubmit = (data: CreateCattleInput) => {
        mutate(data, {
            onSuccess: () => {
                alert('Cattle added successfully!')
                reset()
            },
            onError: () => alert('Failed to add cattle'),
        })
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-2 max-w-sm">
            <label>
                Identifier
                <input type="text" {...register('identifier')} className="border p-1" />
                {errors.identifier && <span className="text-red-500">{errors.identifier.message}</span>}
            </label>
            <button type="submit" disabled={isPending} className="bg-blue-500 text-white p-2">
                {isPending ? 'Adding...' : 'Add Cattle'}
            </button>
        </form>
    )
}
