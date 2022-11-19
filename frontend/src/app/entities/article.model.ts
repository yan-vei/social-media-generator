export class Article {
  constructor(
    public title: string,
    public text: string,
    public url: string,
    public id: number,
    public added_by: string
  ) {}
}
