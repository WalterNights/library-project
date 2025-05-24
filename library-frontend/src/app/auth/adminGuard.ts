import { CanActivateFn, Router } from '@angular/router';

export const adminGuard: CanActivateFn = (route, state) => {
    const user = JSON.parse(localStorage.getItem('user') || '{}');
    if (user && user.rol === 'admin') {
        return true;
    }
    window.location.href = '/';
    return false;
};