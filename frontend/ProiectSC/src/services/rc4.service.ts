import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class Rc4Service {

  constructor(private http:HttpClient) { }

  RC4Encrypt(data:Object):Observable<string>{
    return this.http.post<string>("http://localhost:8000/api/encrypt/rc4",data)
  }

  RC4Decrypt(data:Object):Observable<string>{
    return this.http.post<string>("http://localhost:8000/api/decrypt/rc4",data)
  }
}
