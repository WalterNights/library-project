import { Routes } from '@angular/router';
import { authGuard } from './auth/auth.guard';
import { adminGuard } from './auth/adminGuard';
import { HomeComponent } from './home/home.component';
import { BooksListComponent } from './books-list/books-list.component';
import { BookDetailComponent } from './book-detail/book-detail.component';
import { UserLoanHistoryComponent } from './user-loan-history/user-loan-history.component';
import { AdminDashboardComponent } from './admin-dashboard/admin-dashboard.component';


export const routes: Routes = [
    { path: '', component: HomeComponent, canActivate: [authGuard] },
    { path: 'admin', component: AdminDashboardComponent, canActivate: [authGuard, adminGuard] },
    { path: 'auth', loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule) },
    { path: 'books', component: BooksListComponent },
    { path: 'books/:id', component: BookDetailComponent },
    { path: 'borrow', component: UserLoanHistoryComponent },
];
