import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {API_URL} from '../env';
import {saveAs} from 'file-saver'

@Injectable({
  providedIn: 'root'
})
export class AdminService {

  constructor(private http: HttpClient) { }

  exportFile(file: string) {
    let url: string = `${API_URL}/${file}`
    return this.http.get(url, {responseType: 'blob'});
  }

  exportJson(file: string) {
    this.exportFile(file).subscribe(data => saveAs(data, `${file}.json`));
  }

  
}
