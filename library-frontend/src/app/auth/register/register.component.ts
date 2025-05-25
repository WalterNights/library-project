import { Router } from '@angular/router';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { ModalComponent } from '../../shared/modal/modal.component';


@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, ModalComponent],
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
  showModal = false;

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

    this.http.post<any>(`${environment.apiUrl}/auth/register/`, this.credentials).subscribe({
      next: () => {
        this.success = 'Registro exitoso. ahora puedes iniciar sesión.';
        this.error = '';
        this.showModal = true;
        setTimeout(() => {
          this.showModal = false;
          this.router.navigate(['/auth/login']);
        }, 3000);
      },
      error: err => {
        this.error = err.error?.detail || 'Error al registrar el usuario';
        this.success = '';
      }
    });
  }
}