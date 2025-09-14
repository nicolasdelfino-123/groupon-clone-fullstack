import React, { Component } from "react";

// Detectar automáticamente la URL del backend
const getBackendURL = () => {
    // Si estamos en Vercel (producción)
    if (process.env.NODE_ENV === 'production') {
        // En Vercel, el backend está en la misma URL base pero bajo /api
        return window.location.origin + '/api';
    }
    
    // Para desarrollo local
    return process.env.BACKEND_URL || "http://localhost:3001";
};

// Exportar la URL del backend
export const getAPIHost = () => getBackendURL();

const Dark = ({children}) => <span className="bg-dark text-white px-1 rounded">{children}</span>;

export const BackendURL = () => (
	<div className="mt-5 pt-5 w-50 mx-auto">
		<h2>Backend URL Configuration</h2>
		<div className="alert alert-info">
			<h5>🚀 Current Backend URL:</h5>
			<code>{getBackendURL()}</code>
		</div>
		<div className="alert alert-success">
			<h5>✅ Auto-detection Status:</h5>
			<p>
				<strong>Environment:</strong> {process.env.NODE_ENV || 'development'}<br/>
				<strong>Detection:</strong> Automatic URL detection enabled<br/>
				<strong>Fallback:</strong> localhost:3001 for development
			</p>
		</div>
	</div>
);
