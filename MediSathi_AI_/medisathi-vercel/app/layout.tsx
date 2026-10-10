import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata = { title: 'MediSathi AI | Your Health Companion', description: 'MediSathi AI healthcare companion dashboard and appointment organizer.' };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="en"><body>{children}</body></html>; }
