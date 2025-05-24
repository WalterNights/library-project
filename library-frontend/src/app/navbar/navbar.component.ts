import { Component } from '@angular/core';
import { Location } from '@angular/common';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { AuthService } from '../auth/auth.service';
import { ModalComponent } from '../shared/modal/modal.component';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule, ModalComponent, RouterModule],
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {

  showModal = false;

  constructor(public authService: AuthService, private location: Location) { }

  logout() {
    this.showModal = true;
    setTimeout(() => {
      this.showModal = false;
      this.authService.logout();
    }, 3000);
  }

  goBack() {
    this.location.back();
  }

  isAdmin(): boolean {
  if (typeof window === 'undefined') return false;
  const user = JSON.parse(localStorage.getItem('user') || '{}');
  return user && user.rol === 'admin';
}
}