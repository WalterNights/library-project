import { Router } from '@angular/router';
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-register',
  standalone: false,
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  credentials = { 
    username: '', 
    first_name: '',
    last_name: '',
    email: '',
    password: ''
  };
  confirmPassword = '';
  error = '';
  success = '';

  constructor(private http: HttpClient, private router: Router) {}

  register() {
    if(this.credentials.password.includes(this.credentials.username)) {
      this.error = 'La contraseña no puede contener el nombre de usuario';
      this.success = '';
      return;
    }
    if(this.credentials.password !== this.confirmPassword) {
      this.error = 'Las contraseñas no coinciden';
      this.success = '';
      return;
    }

    this.http.post<any>('http://localhost:8000/auth/register/', this.credentials).subscribe({
      next: () => {
        this.success = 'Registro exitoso. ahora puedes iniciar sesión.';
        this.router.navigate(['/login']);
      },
      error: err => {
        this.error = err.error?.detail || 'Error al registrar el usuario';
        this.success = '';
      }
    });
  }
}