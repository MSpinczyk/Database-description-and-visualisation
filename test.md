```dbml
Table "Album" {
  "AlbumId" INT [not null]
  "Title" VARCHAR(160) [not null]
  "ArtistId" INT [not null]

Indexes {
  AlbumId [pk, name: "PK_Album"]
  ArtistId [name: "IFK_AlbumArtistId"]
}
}

Table "Artist" {
  "ArtistId" INT [not null]
  "Name" VARCHAR(120)

Indexes {
  ArtistId [pk, name: "PK_Artist"]
}
}

Table "Customer" {
  "CustomerId" INT [not null]
  "FirstName" VARCHAR(40) [not null]
  "LastName" VARCHAR(20) [not null]
  "Company" VARCHAR(80)
  "Address" VARCHAR(70)
  "City" VARCHAR(40)
  "State" VARCHAR(40)
  "Country" VARCHAR(40)
  "PostalCode" VARCHAR(10)
  "Phone" VARCHAR(24)
  "Fax" VARCHAR(24)
  "Email" VARCHAR(60) [not null]
  "SupportRepId" INT

Indexes {
  CustomerId [pk, name: "PK_Customer"]
  SupportRepId [name: "IFK_CustomerSupportRepId"]
}
}

Table "Employee" {
  "EmployeeId" INT [not null]
  "LastName" VARCHAR(20) [not null]
  "FirstName" VARCHAR(20) [not null]
  "Title" VARCHAR(30)
  "ReportsTo" INT
  "BirthDate" TIMESTAMP
  "HireDate" TIMESTAMP
  "Address" VARCHAR(70)
  "City" VARCHAR(40)
  "State" VARCHAR(40)
  "Country" VARCHAR(40)
  "PostalCode" VARCHAR(10)
  "Phone" VARCHAR(24)
  "Fax" VARCHAR(24)
  "Email" VARCHAR(60)

Indexes {
  EmployeeId [pk, name: "PK_Employee"]
  ReportsTo [name: "IFK_EmployeeReportsTo"]
}
}

Table "Genre" {
  "GenreId" INT [not null]
  "Name" VARCHAR(120)

Indexes {
  GenreId [pk, name: "PK_Genre"]
}
}

Table "Invoice" {
  "InvoiceId" INT [not null]
  "CustomerId" INT [not null]
  "InvoiceDate" TIMESTAMP [not null]
  "BillingAddress" VARCHAR(70)
  "BillingCity" VARCHAR(40)
  "BillingState" VARCHAR(40)
  "BillingCountry" VARCHAR(40)
  "BillingPostalCode" VARCHAR(10)
  "Total" NUMERIC(10,2) [not null]

Indexes {
  InvoiceId [pk, name: "PK_Invoice"]
  CustomerId [name: "IFK_InvoiceCustomerId"]
}
}

Table "InvoiceLine" {
  "InvoiceLineId" INT [not null]
  "InvoiceId" INT [not null]
  "TrackId" INT [not null]
  "UnitPrice" NUMERIC(10,2) [not null]
  "Quantity" INT [not null]

Indexes {
  InvoiceLineId [pk, name: "PK_InvoiceLine"]
  InvoiceId [name: "IFK_InvoiceLineInvoiceId"]
  TrackId [name: "IFK_InvoiceLineTrackId"]
}
}

Table "MediaType" {
  "MediaTypeId" INT [not null]
  "Name" VARCHAR(120)

Indexes {
  MediaTypeId [pk, name: "PK_MediaType"]
}
}

Table "Playlist" {
  "PlaylistId" INT [not null]
  "Name" VARCHAR(120)

Indexes {
  PlaylistId [pk, name: "PK_Playlist"]
}
}

Table "PlaylistTrack" {
  "PlaylistId" INT [not null]
  "TrackId" INT [not null]

Indexes {
  (PlaylistId, TrackId) [pk, name: "PK_PlaylistTrack"]
  TrackId [name: "IFK_PlaylistTrackTrackId"]
}
}

Table "Track" {
  "TrackId" INT [not null]
  "Name" VARCHAR(200) [not null]
  "AlbumId" INT
  "MediaTypeId" INT [not null]
  "GenreId" INT
  "Composer" VARCHAR(220)
  "Milliseconds" INT [not null]
  "Bytes" INT
  "UnitPrice" NUMERIC(10,2) [not null]

Indexes {
  TrackId [pk, name: "PK_Track"]
  AlbumId [name: "IFK_TrackAlbumId"]
  GenreId [name: "IFK_TrackGenreId"]
  MediaTypeId [name: "IFK_TrackMediaTypeId"]
}
}

Ref "FK_AlbumArtistId":"Artist"."ArtistId" < "Album"."ArtistId" [update: no action, delete: no action]

Ref "FK_CustomerSupportRepId":"Employee"."EmployeeId" < "Customer"."SupportRepId" [update: no action, delete: no action]

Ref "FK_EmployeeReportsTo":"Employee"."EmployeeId" < "Employee"."ReportsTo" [update: no action, delete: no action]

Ref "FK_InvoiceCustomerId":"Customer"."CustomerId" < "Invoice"."CustomerId" [update: no action, delete: no action]

Ref "FK_InvoiceLineInvoiceId":"Invoice"."InvoiceId" < "InvoiceLine"."InvoiceId" [update: no action, delete: no action]

Ref "FK_InvoiceLineTrackId":"Track"."TrackId" < "InvoiceLine"."TrackId" [update: no action, delete: no action]

Ref "FK_PlaylistTrackPlaylistId":"Playlist"."PlaylistId" < "PlaylistTrack"."PlaylistId" [update: no action, delete: no action]

Ref "FK_PlaylistTrackTrackId":"Track"."TrackId" < "PlaylistTrack"."TrackId" [update: no action, delete: no action]

Ref "FK_TrackAlbumId":"Album"."AlbumId" < "Track"."AlbumId" [update: no action, delete: no action]

Ref "FK_TrackGenreId":"Genre"."GenreId" < "Track"."GenreId" [update: no action, delete: no action]

Ref "FK_TrackMediaTypeId":"MediaType"."MediaTypeId" < "Track"."MediaTypeId" [update: no action, delete: no action]

```