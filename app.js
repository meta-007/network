app.post('/update/:id', routes.update);
app.post('/import', routes.import);
app.get('/about_new', routes.about_new);
app.get('/chat', routes.chat.get);
app.put('/chat', routes.chat.add);
app.delete('/chat', routes.chat.delete);
app.use('/users', routesUsers)

//static
app.use(st({path: './public', url:'/public'}));

marked.setOptions({sanitize:true});
app.locals.marked = marked;

if (app.get('env') === 'development') {
    app.use(error(errorHandler()));
}
