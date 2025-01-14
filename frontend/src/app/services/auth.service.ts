import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {tap} from 'rxjs/operators'

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:8000/';
  private tokenKey = 'authToken';

  constructor(private http: HttpClient) {
  }

  login(credentials: { email: string, password: string }): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/login`, credentials).pipe(tap(response => {
      // Almacenar el token en el almacenamiento local
      localStorage.setItem(this.tokenKey, response.token);
    }));
  }

  logout(): void{
    localStorage.removeItem(this.tokenKey);
  }

  isAuthenticated(): boolean{
    return this.tokenKey === this.tokenKey;
  }
}


