# MediSathi AI — Vercel + Supabase starter

Premium responsive healthcare dashboard built with Next.js, React, TypeScript, and Supabase Auth/Postgres. Intended for hackathon/demo use; it is not a medical diagnosis tool and does not contact real clinics.

## Features
- Email/password sign-up and sign-in with Supabase Auth
- Responsive dashboard, sidebar navigation, mobile menu, appointment modal
- Appointments saved to Supabase when configured and signed in
- Row Level Security policy SQL so each user can access only their own appointments
- Local preview mode when Supabase credentials are absent (appointments are only in browser memory in this mode)

## Run locally
1. Install Node.js LTS.
2. Extract ZIP, open the folder in VS Code/terminal.
3. Run `npm install`.
4. Copy `.env.example` to `.env.local` and set your Supabase project URL and anon/publishable key.
5. In Supabase SQL Editor, run all of `supabase-schema.sql`.
6. Run `npm run dev` and open `http://localhost:3000`.

## Supabase setup
1. Create a project at https://supabase.com/.
2. Find the Project URL and anon/publishable key in project API/connect settings.
3. Put them in `.env.local`:
   - `NEXT_PUBLIC_SUPABASE_URL=...`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY=...`
4. Run `supabase-schema.sql` in SQL Editor.
5. In Authentication settings, set your local and deployed site URLs / redirect URLs. For email-confirmation flows, confirm the email before signing in.

## Deploy to Vercel
1. Push the extracted project to a GitHub repository.
2. In https://vercel.com/ choose Add New → Project and import the repository.
3. Add Environment Variables in Project Settings → Environment Variables:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
4. Deploy. After deployment, add the Vercel URL to Supabase Auth's Site URL and allowed redirect URLs, then redeploy if needed.

## Notes
- The Vercel deployment is not created automatically by this ZIP; you must connect your own GitHub/Vercel accounts and add your Supabase credentials.
- Never put Supabase service-role keys in `NEXT_PUBLIC_*` variables or client-side code.
- The current appointment form is a demo organizer. Real doctor discovery, clinic integrations, medical records, notifications, and AI medical functionality are not implemented here.
