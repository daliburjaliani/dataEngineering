-- select top 3 genres by sale
SELECT G.Name Ganre,
       SUM(INL.UnitPrice) TotalSales
FROM InvoiceLine INL
LEFT JOIN Invoice ON Invoice.InvoiceId = INL.InvoiceId
LEFT JOIN Track T on inl.TrackId = T.TrackId
LEFT JOIN Genre G ON G.GenreId = T.GenreId
GROUP BY G.GenreId
ORDER BY TotalSales DESC
LIMIT 3;

-- Employee Sales Performance
SELECT E.FirstName,
       E.LastName,
       SUM(Total) TotalSales
FROM Employee E
LEFT JOIN Customer C on E.EmployeeId = C.SupportRepId
LEFT JOIN Invoice I on C.CustomerId = I.CustomerId
GROUP BY E.EmployeeId
ORDER BY TotalSales DESC;

-- Popular Playlists
-- get distinct playlist names cause in playlist track same track have different id that are same playlist name
SELECT DISTINCT PL.Name,
                COUNT(PT.TrackId) Tracks
FROM Playlist PL
LEFT JOIN PlaylistTrack PT ON PL.PlaylistId = PT.PlaylistId
GROUP BY PL.PlaylistId
ORDER BY Tracks DESC
LIMIT 5;

-- Customer Purchase Analysis
SELECT C.FirstName,
       C.LastName,
       COUNT(I.InvoiceId) Purchase
FROM Customer C
LEFT JOIN Invoice I on C.CustomerId = I.CustomerId
GROUP BY C.CustomerId
ORDER BY Purchase DESC ;