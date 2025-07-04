"use client";
import { useAuth } from "react-oidc-context";

export function AuthButtons() {
  const auth = useAuth();

  if (auth.isLoading) return <p>Loading...</p>;
  if (auth.error) return <p>Error: {auth.error.message}</p>;

  return auth.isAuthenticated ? (
    <>
      <p>Welcome, {auth.user?.profile.email}</p>
      <button onClick={() => auth.signoutRedirect().then(() =>{
        window.location.href="http://localhost:3000"
      })}>Logout</button>
    </>
  ) : (
    <button onClick={() => auth.signinRedirect()}>Login</button>
  );
}
