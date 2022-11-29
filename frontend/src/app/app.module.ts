import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { TooltipModule } from 'ngx-bootstrap/tooltip';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { AuthService } from './services/auth.service';
import { ArticleService } from './services/article.service';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { RegisterComponent } from './components/register/register.component';
import { HomeComponent } from './components/home/home.component';
import { GeneratorComponent } from './components/generator/generator.component';
import { EnsureAuthenticated } from './services/ensure-authenticated.service';
import { TweetsComponent } from './components/tweets/tweets.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { HistoryComponent } from './components/history/history.component';
import { TextService } from './services/text.service';
import { GeneratorService } from './services/generator.service';
import { LogoutService } from './services/logout.service';
import { AdminPanelComponent } from './components/admin/admin-panel/admin-panel.component';
import { EnsureAdmin } from './services/ensure-admin.service';
import { AllHistoryComponent } from './components/admin/all-history/all-history.component';
import { ConfigurationComponent } from './components/admin/configuration/configuration.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    HomeComponent,
    GeneratorComponent,
    TweetsComponent,
    SidebarComponent,
    HistoryComponent,
    AllHistoryComponent,
    ConfigurationComponent,
    AdminPanelComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    TooltipModule.forRoot(),
    RouterModule.forRoot([
      { path: '', component: HomeComponent},
      { path: 'login', component: LoginComponent },
      { path: 'register', component: RegisterComponent},
      { path: 'generator', component: GeneratorComponent, canActivate: [EnsureAuthenticated]},
      { path: 'history', component: HistoryComponent, canActivate: [EnsureAuthenticated]},
      { path:'admin/all-history', component: AllHistoryComponent, canActivate: [EnsureAuthenticated, ]},
      { path:'admin/configuration', component: ConfigurationComponent, canActivate: [EnsureAuthenticated, ]},
      { path: 'admin', component: AdminPanelComponent, canActivate: [EnsureAuthenticated, ]},
    ])
  ],
  providers: [
    AuthService,
    ArticleService,
    TextService,
    GeneratorService,
    LogoutService,
    EnsureAuthenticated,
    EnsureAdmin
  ],
  bootstrap: [AppComponent]
})

export class AppModule { }
