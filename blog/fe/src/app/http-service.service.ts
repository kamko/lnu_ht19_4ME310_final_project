import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from './../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  public get(path: string) {
    console.log(`get to ${path}`)
    return this.http.get(`${this.baseUrl}${path}`);
  }

  public post(path: string, body: any) {
    console.log(`post to ${path} with ${body}`);
    return this.http.post(`${this.baseUrl}${path}`, body);
  }

  public put(path: string, body: any) {
    console.log(`put to ${path} with ${body}`);
    return this.http.put(`${this.baseUrl}${path}`, body);
  }
}
