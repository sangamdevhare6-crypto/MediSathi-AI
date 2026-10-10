-- Run this in Supabase Dashboard > SQL Editor.
-- Appointments are private: each authenticated user can only access their own rows.
create table if not exists public.appointments (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  doctor text not null,
  specialty text not null,
  date date not null,
  time text not null,
  status text not null default 'Confirmed',
  created_at timestamptz not null default now()
);
alter table public.appointments enable row level security;
drop policy if exists "Users can read own appointments" on public.appointments;
create policy "Users can read own appointments" on public.appointments for select to authenticated using ((select auth.uid()) = user_id);
drop policy if exists "Users can create own appointments" on public.appointments;
create policy "Users can create own appointments" on public.appointments for insert to authenticated with check ((select auth.uid()) = user_id);
drop policy if exists "Users can update own appointments" on public.appointments;
create policy "Users can update own appointments" on public.appointments for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
drop policy if exists "Users can delete own appointments" on public.appointments;
create policy "Users can delete own appointments" on public.appointments for delete to authenticated using ((select auth.uid()) = user_id);
