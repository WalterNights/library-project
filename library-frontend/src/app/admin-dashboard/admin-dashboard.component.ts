import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ModalComponent } from '../shared/modal/modal.component';

@Component({
  selector: 'app-admin-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule, ModalComponent],
  templateUrl: './admin-dashboard.component.html',
  styleUrls: ['./admin-dashboard.component.css']
})
export class AdminDashboardComponent implements OnInit {

  users: any[] = [];
  books: any[] = [];
  showUserDetails = false;
  selectedUser: any = null;
  selectedUserHistory: any[] = [];

  viewMode: 'users' | 'books' = 'users';

  showModal = false;
  showBookCreateModal = false;
  showBulkCreateModal = false;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    const token = localStorage.getItem('access_token');
    this.http.get<any>('/users/', {
      headers: { Authorization: `Bearer ${token}` }
    }).subscribe(users => this.users = users);

    this.http.get<any>('/books/', {
      headers: { Authorization: `Bearer ${token}` }
    }).subscribe(books => {
      this.books = books;
    });
  }

  showUsers() {
    this.viewMode = 'users';
  }

  showBooks() {
    this.viewMode = 'books';
  }

  viewUserDetails(user: any) {
    this.selectedUser = user;
    this.showUserDetails = true;
    const token = localStorage.getItem('access_token');
    this.http.get<any[]>(`/api/users/${user.id}/history`, {
      headers: { Authorization: `Bearer ${token}` }
    }).subscribe(history => {
      this.selectedUserHistory = history;
    });
  }

  newBook = { title: '', author: '', year_publication: '', stock: '' };

  createBook() {
    const token = localStorage.getItem('access_token');
    this.showModal = true;
    this.http.post('/api/books/', this.newBook, {
      headers: { Authorization: `Bearer ${token}` }
    }).subscribe(() => {
      this.closeModalBookCreate();
      // Recarga la lista de libros
      this.http.get<any>('/api/books/', {
        headers: { Authorization: `Bearer ${token}` }
      }).subscribe(books => {
        this.books = books;
        setTimeout(() => {
          this.showModal = false;
        }, 3000);
      });
    });
  }

  bulkFile: File | null = null;

  onBulkFileChange(event: any) {
    this.bulkFile = event.target.files[0];
  }

  bulkCreateBooks() {
    if (this.bulkFile) {
      const formData = new FormData();
      formData.append('file', this.bulkFile);
      const token = localStorage.getItem('access_token');
      this.showModal = true;
      this.http.post('/api/books/bulk_upload/', formData, {
        headers: { Authorization: `Bearer ${token}` }
      }).subscribe(() => {
        this.closeModalBulkCreate();
        // Recarga la lista de libros
        this.http.get<any>('/api/books/', {
          headers: { Authorization: `Bearer ${token}` }
        }).subscribe(books => {
          this.books = books;
          setTimeout(() => {
            this.showModal = false;
          }, 3000);
        });
      });
    }
  }

  editBookModal = false;
  bookToEdit: any = null;

  openEditBookModal(book: any) {
    this.bookToEdit = { ...book };
    this.editBookModal = true;
  }

  closeEditBookModal() {
    this.editBookModal = false;
    this.bookToEdit = null;
  }

  updateBook() {
    const token = localStorage.getItem('access_token');
    this.showModal = true;
    this.http.put(`/api/books/${this.bookToEdit.id}/`, this.bookToEdit, {
      headers: { Authorization: `Bearer ${token}` }
    }).subscribe(() => {
      this.editBookModal = false;
      this.bookToEdit = null;
      // Recarga la lista de libros
      this.http.get<any>('/api/books/', {
        headers: { Authorization: `Bearer ${token}` }
      }).subscribe(books => {
        this.books = books;
        setTimeout(() => {
          this.showModal = false;
        }, 2000);
      });
    });
  }

  closeUserDetails() {
    this.showUserDetails = false;
    this.selectedUser = null;
  }

  openModalBookCreate() {
    this.showBookCreateModal = true;
  }

  closeModalBookCreate() {
    this.showBookCreateModal = false;
  }

  openModalBulkCreate() {
    this.showBulkCreateModal = true;
  }

  closeModalBulkCreate() {
    this.showBulkCreateModal = false;
  }
}
