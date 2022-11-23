import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable} from 'rxjs';
import {API_URL} from '../env';
import {saveAs} from 'file-saver'

@Injectable({
  providedIn: 'root'
})
export class AdminService {

  constructor(private http: HttpClient) { }

  exportFile(file: string) {
    let url: string = `${API_URL}/configs?filename=${file}`
    return this.http.get(url, {responseType: 'blob'});
  }

  exportJson(file: string) {
    this.exportFile(file).subscribe(data => saveAs(data, `${file}`));
  }

  uploadFile(file: File): Observable<any> {
    let url: string = `${API_URL}/configs`

    const formData = new FormData();

    formData.append("file", file);

    return this.http.post(url, formData);
  }

  deleteArticle(id: string): Observable<any> {
    let url: string = `${API_URL}/articles/id?=${id}`
    return this.http.delete(url)
  }

  deleteText(id: string): Observable<any> {
    let url: string = `${API_URL}/text-extracts/id?=${id}`
    return this.http.delete(url)
  }
}
