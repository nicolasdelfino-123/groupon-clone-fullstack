// src/front/js/api.js
export const API_BASE = (
  import.meta?.env?.VITE_API_BASE ||
  process.env.REACT_APP_API_BASE ||
  "/api"
).replace(/\/+$/, ""); // quita barra final

export const apiFetch = (path, opts = {}) =>
  fetch(`${API_BASE}${path.startsWith("/") ? path : `/${path}`}`, {
    headers: { "Content-Type": "application/json", ...(opts.headers || {}) },
    ...opts,
  });
