"use client";
import { AuthProvider } from "react-oidc-context";
import React from "react";

const oidcConfig = {
  authority: process.env.NEXT_PUBLIC_OIDC_AUTHORITY!,
  client_id: process.env.NEXT_PUBLIC_OIDC_CLIENT_ID!,
  redirect_uri: process.env.NEXT_PUBLIC_OIDC_REDIRECT_URI!,
  post_logout_redirect_uri: "http://localhost:3000",
  response_type: "code",
};

export function OidcWrapper({ children }: { children: React.ReactNode }) {
  return <AuthProvider {...oidcConfig}>{children}</AuthProvider>;
}
