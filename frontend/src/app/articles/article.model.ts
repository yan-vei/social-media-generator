export class Article {
  constructor(
    public title: string,
    public text: string,
    public url: string,
    public header: string,
    public author: string,
    public published_on: Date,
    public id?: number,
    public created_at?: Date,
    public added_by?: string
  ) {}
}
