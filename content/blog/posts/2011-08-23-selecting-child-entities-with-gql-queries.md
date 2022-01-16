---
title: Selecting Child Entities with GQL Queries
author: matt
type: post
date: 2011-08-23T17:14:36+00:00
url: /blog/2011/08/23/selecting-child-entities-with-gql-queries/
categories:
  - Uncategorized

---
In [Google App Engine][1], you can create [owned one-to-many relationships][2] between entities. The classic example you were taught at uni is that a Book owns a Chapter, which in turn, owns a Paragraph. For my site, [stolencamerafinder][3], the example is that a camera Make owns a set of Models.

If you want to query for the model directly in GQL (from the app engine dashboard for example) you can create the key by specifying the full parent chain:

```
SELECT * FROM Model where __key__ = KEY('Make', 'canon', 'Model', 'canon eos 5d')
```

Google’s [GQL reference][4] was a little sparse on this syntax so I’m posting it here in the hope you find this faster than I worked it out.

For completeness, this is the difference it makes in JDO. My old code looked something like this:

```
PersistenceManager pm = PMF.get().getPersistenceManager();
Key makeKey = KeyFactory.createKey(Make.class.getSimpleName(), makeName);
Make make = pm.getObjectById(Make.class, key);List<Model> models = make.getModels();

for (Model model : models) {
    if (model.getName().equals(modelName)) {
        return model;
    }
}
```

It doesn’t take much imagination to realise this doesn’t scale very nicely as the number of models increases. The new code looks like this:

```
PersistenceManager pm = PMF.get().getPersistenceManager();


Key makeKey = KeyFactory.createKey(Make.class.getSimpleName(), makeName);


// Can create the Model key by specifying parent key...


Key modelKey = KeyFactory.createKey(makeKey, Model.class.getSimpleName(), name);


// Bam! Get the child entity in a single query


Model model = pm.getObjectById(Model.class, modelKey);
```

I wouldn’t have noticed this performance bottle neck if it wasn’t for [appwrench][5]. It looks a little dead to be honest, but works well.

 [1]: http://code.google.com/appengine/
 [2]: http://code.google.com/appengine/docs/java/datastore/jdo/relationships.html#Owned_One_to_Many_Relationships
 [3]: http://www.stolencamerafinder.com
 [4]: http://code.google.com/appengine/docs/python/datastore/gqlreference.html
 [5]: http://appwrench.onpositive.com/