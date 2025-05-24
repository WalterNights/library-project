import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

import { LoginComponent } from './login/login.component';
import { AuthRoutingModule } from './auth-routing.module';
import { RegisterComponent } from './register/register.component';

@NgModule({
  declarations: [],
  imports: [
    FormsModule,
    CommonModule,
    LoginComponent,
    RegisterComponent,
    AuthRoutingModule
  ]
})
export class AuthModule {}
